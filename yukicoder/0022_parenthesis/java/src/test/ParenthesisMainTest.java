package test;

import static org.hamcrest.CoreMatchers.*;
import static org.hamcrest.MatcherAssert.*;
import main.ParenthesisMain;

import org.junit.Before;
import org.junit.Test;

public class ParenthesisMainTest {

    ParenthesisMain parenthesisMain;

    @Before
    public void setUp() {
        parenthesisMain = new ParenthesisMain();
    }

    @Test
    public void test01() {
        String[] args = { "4", "4", "(())" };
        int expected = 1;
        int actual = parenthesisMain.execute(args);
        assertThat(actual, is(expected));
    }

    @Test
    public void test02() {
        String[] args = { "12", "2", "(((())()()))" };
        int expected = 11;
        int actual = parenthesisMain.execute(args);
        assertThat(actual, is(expected));
    }

    @Test
    public void test03() {
        String[] args = { "20", "5", "((((((()))))))(()())" };
        int expected = 10;
        int actual = parenthesisMain.execute(args);
        assertThat(actual, is(expected));
    }
}
