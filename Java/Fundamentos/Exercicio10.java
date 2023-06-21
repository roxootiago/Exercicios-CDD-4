package Fundamentos;
import java.util.Scanner;

public class Exercicio10 {

	public static void main(String[] args) {
		Scanner inp = new Scanner(System.in);
		System.out.print("Digite o primeiro numero: ");
		int nume1 = inp.nextInt();
		
		System.out.print("Digite o segundo numero: ");
		int nume2 = inp.nextInt();
	
		System.out.print("Digite o terceiro numero: ");
		int nume3 = inp.nextInt();
		
		if (nume1 > nume2 && nume1 > nume3) {
			System.out.println(nume1+" e maior que " + nume2 + " e " + nume3);
		}
		else if (nume2 > nume1 && nume2 > nume3) {
			System.out.println(nume2+" e maior que " + nume1 + " e " + nume3);
		}
			
		else {
			System.out.println(nume3 + " e maior que " + nume1 + " e " + nume2);
			}
		}
	}


