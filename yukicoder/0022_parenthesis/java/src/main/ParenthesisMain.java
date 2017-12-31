package main;

public class ParenthesisMain {

    private Arguments arguments;

    public static void main(String[] args) {
        new ParenthesisMain().execute(args);
    }

    public int execute(String[] args) {
        setArguments(args);
        return analyze();
    }

    private int analyze() {

        String[] parensArray = arguments.getParens().split("");
        int targetArrayIndex = arguments.getTargetIndex() - 1;
        String comparedParen = parensArray[targetArrayIndex];

        Parenthesis parenthesis = createInstance(comparedParen, parensArray,
                targetArrayIndex);
        return parenthesis.findPareParenIndex();
    }

    private void setArguments(String[] args) {
        int parenCount = Integer.valueOf(args[0]);
        int targetIndex = Integer.valueOf(args[1]);
        String parens = args[2];
        arguments = new Arguments(parenCount, targetIndex, parens);
    }

    private abstract class Parenthesis {

        private String paren;
        private String[] parensArray;
        int targetArrayIndex;

        public Parenthesis(String paren, String[] parensArray,
                int targetArrayIndex) {
            this.paren = paren;
            this.parensArray = parensArray;
            this.targetArrayIndex = targetArrayIndex;
        }

        public int findPareParenIndex() {
            int pareCount = 1;
            for (int i = 0; i < parensArray.length; i++) {
                int currentIndex = getCurrentIndex(i, targetArrayIndex);

                pareCount = calcPareCount(pareCount, parensArray[currentIndex]);
                if (pareCount == 0) {
                    return currentIndex + 1;
                }
            }
            return -1;
        }

        private int calcPareCount(int pareCount, String paren) {
            return paren.equals(this.paren) ? ++pareCount : --pareCount;
        }

        protected abstract int getCurrentIndex(int index, int targetArrayIndex);
    }

    private class LeftParenthesis extends Parenthesis {

        public LeftParenthesis(String paren, String[] parensArray,
                int targetArrayIndex) {
            super(paren, parensArray, targetArrayIndex);
        }

        @Override
        protected int getCurrentIndex(int index, int targetArrayIndex) {
            return index + (targetArrayIndex + 1);
        }
    }

    private class RightParenthesis extends Parenthesis {

        public RightParenthesis(String paren, String[] parensArray,
                int targetArrayIndex) {
            super(paren, parensArray, targetArrayIndex);
        }

        @Override
        protected int getCurrentIndex(int index, int targetArrayIndex) {
            return targetArrayIndex - (index + 1);
        }
    }

    public Parenthesis createInstance(String paren, String[] parensArray,
            int targetArrayIndex) {
        switch (paren) {
        case "(":
            return new LeftParenthesis(paren, parensArray, targetArrayIndex);
        case ")":
            return new RightParenthesis(paren, parensArray, targetArrayIndex);
        default:
            throw new IllegalArgumentException();
        }
    }

    private class Arguments {

        private final int parenCount;
        private final int targetIndex;
        private final String parens;

        public Arguments(int parenCount, int targetIndex, String parens) {
            this.parenCount = parenCount;
            this.targetIndex = targetIndex;
            this.parens = parens;
        }

        public int getParenCount() {
            return parenCount;
        }

        public int getTargetIndex() {
            return targetIndex;
        }

        public String getParens() {
            return parens;
        }
    }

}
