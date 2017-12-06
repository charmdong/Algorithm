package com.Java.ex;

public class PG_FindKim {
	public String findKim(String[] seoul) {
		int x = 0;
		for(x=0; x<seoul.length;x++)
			if("Kim" == seoul[x])
				break;
		return "김서방은 " + (x+1) + "에 있다.";
	}
}
