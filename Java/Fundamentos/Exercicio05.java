package Fundamentos;

public class Exercicio05 {
	public static void manin(String[] args) {
	int a = 3;
	int b = 4;
	int c = 7;
	
	if(a++ >= b)
		System.out.println(--c);
		
	else
		System.out.println(c++);
	}
}