package Fundamentos;
import java.util.Scanner;

public class Exercicio11 {

	public static void main(String[] args) {

		Scanner inp = new Scanner(System.in);
		System.out.print("Digite o primeiro número: ");
		int num1 = inp.nextInt();
		
		System.out.print("Digite o segundo número: ");
		int num2 = inp.nextInt();
		
		System.out.print("Digite o terceiro número: ");
		int num3 = inp.nextInt();
		
		System.out.println(num1 > num2 && num1 > num3 ? num1 + " e o maior": num2 > num1 && num2 > num3 ? num2 + " e o maior"
				: num3 + "e o maior");
	}

}
