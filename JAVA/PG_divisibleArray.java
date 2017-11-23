package com.Java.ex;

import java.util.Arrays;

class PG_divisibleArray {
	public int[] divisible(int[] array, int divisor) {

		return Arrays.stream(array).filter(fac -> fac%divisor ==0).toArray();
	}
	// 아래는 테스트로 출력해 보기 위한 코드입니다.
	public static void main(String[] args) {
		PG_divisibleArray div = new PG_divisibleArray();
		int[] array = {5, 9, 7, 10};
		System.out.println( Arrays.toString( div.divisible(array, 5) ));
	}
}