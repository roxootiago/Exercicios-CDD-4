package Fundamentos;
import java.util.Scanner;

public class Exercicio08 {

	public static void main(String[] args) {
		Scanner nickname = new Scanner(System.in);
		System.out.print("Digite um nome: ");
		String respo = nickname.nextLine();//Recebe com espaços e tudo
		System.out.println("Ola, " + respo);
		
		Scanner idade = new Scanner(System.in);
		System.out.print("Digite sua idade:");
		int idd = idade.nextInt();
		System.out.println("Idade: " + idd);
	}

}
