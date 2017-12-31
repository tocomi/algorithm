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
        int pareCount = 1;
        switch (parensArray[targetArrayIndex]) {
        case "(":
            for (int i = targetArrayIndex + 1; i < parensArray.length; i++) {
                switch (parensArray[i]) {
                case "(":
                    pareCount++;
                    break;
                case ")":
                    pareCount--;
                    break;
                default:
                    break;
                }
                if (pareCount == 0) {
                    return i + 1;
                }
            }
            break;
        case ")":
            for (int i = targetArrayIndex - 1; i >= 0; i--) {
                switch (parensArray[i]) {
                case "(":
                    pareCount--;
                    break;
                case ")":
                    pareCount++;
                    break;
                default:
                    break;
                }
                if (pareCount == 0) {
                    return i + 1;
                }
            }
            break;
        default:
            break;
        }

        return -1;
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

}
