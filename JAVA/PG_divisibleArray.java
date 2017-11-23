package com.Java.ex;

import java.util.Arrays;

class PG_divisibleArray {
	public int[] divisible(int[] array, int divisor) {

		return Arrays.stream(array).filter(fac -> fac%divisor ==0).toArray();
	}
	// �Ʒ��� �׽�Ʈ�� ����� ���� ���� �ڵ��Դϴ�.
	public static void main(String[] args) {
		PG_divisibleArray div = new PG_divisibleArray();
		int[] array = {5, 9, 7, 10};
		System.out.println( Arrays.toString( div.divisible(array, 5) ));
	}
}