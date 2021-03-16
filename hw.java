
public class hw {
  public static void main(String[] args){
    String number = "482";
    int a0 = number.charAt(2) - '0';
    int a1 = (number.charAt(1) - '0') * 10;
    int a2 = (number.charAt(0) - '0') * 100;

    System.out.println(a0 + a1 + a2);
  }
}
