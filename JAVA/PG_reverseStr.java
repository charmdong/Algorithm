package com.Java.ex;

import java.util.Arrays;

public class PG_reverseStr {
	public String reverseStr(String str){
		char[] tmp = str.toCharArray();
		Arrays.sort(tmp);
		str = String.valueOf(tmp);
		return new StringBuffer(str).reverse().toString();
	}

	// 아래는 테스트로 출력해 보기 위한 코드입니다.
	public static void main(String[] args) {
		PG_reverseStr rs = new PG_reverseStr();
		System.out.println( rs.reverseStr("Zbcdefg") );
	}
}
