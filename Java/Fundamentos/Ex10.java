package Fundamentos;
import java.util.Scanner;

public class Ex10 {

	public static void main(String[] args) {
		Scanner num = new Scanner(System.in);
		System.out.print("Digite um numero: ");
		int numero = num.nextInt();
		
		System.out.println(numero > 0 ? numero + " e positivo" : numero == 0 ? numero + " e neutro" :numero + " e negativo");
		
	}

}
