package Fundamentos;
import java.util.Scanner;

public class Exercicios09 {

	public static void main(String[] args) {
		Scanner num = new Scanner(System.in);
		System.out.print("Digite um numero: ");
		int numero = num.nextInt();
		
		if (numero > 0 || numero != 0){
			System.out.println(numero + " e positivo");
		}
		else {
			System.out.println(" e negativo");
		}
		

	}

}
