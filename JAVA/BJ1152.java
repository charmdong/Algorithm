package com.Java.ex;

import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class BJ1152 {
	public static void main(String[] args) {
		Set<String> set = new HashSet<String>();
		Scanner scan = new Scanner(System.in);
		String str;
		String[] array;
		
		str = scan.nextLine();
		scan.close();
		
		array = str.split(" ");
		
		for(String tmp : array)
			set.add(tmp);
		
		System.out.println(set.size());
	}
}
