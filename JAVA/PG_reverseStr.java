package com.Java.ex;

import java.util.Arrays;

public class PG_reverseStr {
	public String reverseStr(String str){
		char[] tmp = str.toCharArray();
		Arrays.sort(tmp);
		str = String.valueOf(tmp);
		return new StringBuffer(str).reverse().toString();
	}

	// �Ʒ��� �׽�Ʈ�� ����� ���� ���� �ڵ��Դϴ�.
	public static void main(String[] args) {
		PG_reverseStr rs = new PG_reverseStr();
		System.out.println( rs.reverseStr("Zbcdefg") );
	}
}
