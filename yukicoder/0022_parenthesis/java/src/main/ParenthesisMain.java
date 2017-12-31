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

    private abstract class Parenthesis {

        private String[] parensArray;
        int targetArrayIndex;

        public Parenthesis(String[] parensArray, int targetArrayIndex) {
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

        protected abstract int getCurrentIndex(int index, int targetArrayIndex);

        protected abstract int calcPareCount(int pareCount, String paren);
    }

    private class LeftParenthesis extends Parenthesis {

        public LeftParenthesis(String[] parensArray, int targetArrayIndex) {
            super(parensArray, targetArrayIndex);
        }

        @Override
        protected int getCurrentIndex(int index, int targetArrayIndex) {
            return index + (targetArrayIndex + 1);
        }

        @Override
        protected int calcPareCount(int pareCount, String paren) {
            switch (paren) {
            case "(":
                return ++pareCount;
            case ")":
                return --pareCount;
            default:
                throw new IllegalArgumentException();
            }
        }
    }

    private class RightParenthesis extends Parenthesis {

        public RightParenthesis(String[] parensArray, int targetArrayIndex) {
            super(parensArray, targetArrayIndex);
        }

        @Override
        protected int getCurrentIndex(int index, int targetArrayIndex) {
            return targetArrayIndex - (index + 1);
        }

        @Override
        protected int calcPareCount(int pareCount, String paren) {
            switch (paren) {
            case "(":
                return --pareCount;
            case ")":
                return ++pareCount;
            default:
                throw new IllegalArgumentException();
            }
        }
    }

    public Parenthesis createInstance(String paren, String[] parensArray,
            int targetArrayIndex) {
        switch (paren) {
        case "(":
            return new LeftParenthesis(parensArray, targetArrayIndex);
        case ")":
            return new RightParenthesis(parensArray, targetArrayIndex);
        default:
            throw new IllegalArgumentException();
        }
    }

}
