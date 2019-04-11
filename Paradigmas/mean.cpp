#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int main ()
{
	int i, n;
	float *v, total = 0;
	float med, var = 0;
	n = 10;
	// scanf("%d", &n);
	v = (float*) malloc(n*sizeof(float));
	if (v == NULL)
	{
		printf("Memoria Insuficiente./n");
		return 1;
	}
	else
	{
		for (i = 0; i < n; i ++)
		{
			// scanf("%f", &v[i]);
			v[i] = i;
			total += v[i];
		}
	}
	med = total/n;
	printf("Média : %f \n", med);
	for (int j = 0 ; j < n; j++ ) var = var + pow((v[j]-med), 2);
  	var /= n;
  	printf("Variância: %f \n", var);
	free(v);
	return 0;
}