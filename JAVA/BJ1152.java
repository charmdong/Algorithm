package com.Java.ex;

import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class BJ1152 {
	public static void main(String[] args) {
		Set<String> set = new HashSet<String>();
		Scanner scan = new Scanner(System.in);
		String str;
		
		str = scan.nextLine();
		scan.close();
		int check;
		
		check = str.indexOf(' ');
		
		while(check != -1) {
			set.add(str.substring(0, check));
			str = str.substring(check+1);
			check = str.indexOf(' ');
		}
		set.add(str);
		
		System.out.println(set.size());
	}
}
