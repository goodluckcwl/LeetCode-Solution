#include <stdio.h>
#include <stdlib.h>

//���ֲ��ҡ�
int divide(int dividend, int divisor) {
	int MAX_INT = 2147483647;
	int MIN_INT = -2147483648;
	// ��Ϊ�����붼ת��������������Ҫ��������һЩ����������
	// �����MIN_INT / -1
	if (dividend == MIN_INT && divisor == -1) {
		return MAX_INT;
	}
	// x/MIN_INT = 0
	if (divisor == MIN_INT) {
		if (dividend != MIN_INT) {
			return 0;
		}
		// MIN_INT/MIN_INT = 1
		else {
			return 1;
		}
	}
	// MIN_INT/x,Ϊ�˷�ֹ������ȼ�һ
	int add_one = 0;
	if (dividend == MIN_INT) {
		dividend += 1;
		add_one = 1;
	}

	if (dividend == 0 ) {
		return 0;
	}
	int positive = -1;
	if (dividend < 0 && divisor < 0) {
		dividend = -dividend;
		divisor = -divisor;
		positive = 1;
	}
	if (dividend > 0 && divisor > 0) {
		positive = 1;
	}
	if (dividend < 0 && divisor > 0) {
		dividend = -dividend;
		positive = -1;
	}
	if (dividend > 0 && divisor < 0) {
		divisor = -divisor;
		positive = -1;
	}

	if (dividend < divisor) {
		return 0;
	}

	int n_power = 0;
	int result = 0;
	int divisor_mul = divisor;
	while (dividend - divisor_mul >= 0 && n_power < 31) {
		n_power++;
		divisor_mul = divisor_mul << 1;
	}
	// �в�
	int res = dividend - (divisor << (n_power - 1));
	res = add_one == 1 ? res + 1 : res;
	int count = -1;
	if (res >= divisor) {
		// �в�ݹ����
		count = divide(res, divisor);
		result = (1 << n_power - 1) + count;
	}
	// ���ؽ��
	else {
		result = (1 << n_power - 1);
	}
	
	return positive == 1 ? result : -result;
}

int main() {

	int x1 = divide(10, 3);
	int x2 = divide(10, 45);
	int x3 = divide(-10, 3);
	int x4 = divide(-10, -3);
	int x5 = divide(-2147483648, 2);
	int x6 = divide(1073741823, 1);
	int x7 = divide(2147483647, 1);
	return 0;
}