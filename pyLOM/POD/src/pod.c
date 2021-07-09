/*
	POD - C Functions to compute POD
*/

#include <stdlib.h>

#include "lapacke.h"
#include "pod.h"

// Macros to access flattened matrices
#define MIN(a,b)    ((a)<(b)) ? (a) : (b)
#define AC_X(i,j)   X[n*ii+jj]
#define AC_OUT(i,j) out[n*ii+jj]


void compute_temporal_mean(double *out, double *X, const int m, const int n) {
	/*
		Temporal mean of matrix X(m,n) where m is the spatial coordinates
		and n is the number of snapshots.

		out(m,n) is the output matrix that must have been previously allocated.
	*/
}

void subtract_temporal_mean(double *out, double *X, double *X_mean, const int m, const int n) {
	/*
		Computes out(m,n) = X(m,n) - X_mean(m) where m is the spatial coordinates
		and n is the number of snapshots.
		
		out(m,n) is the output matrix that must have been previously allocated.
	*/
}

void single_value_decomposition(double *U, double *S, double *V, double *Y, const int m, const int n) {
	/*
		Single value decomposition (SVD) using Lapack.

		U(m,n)   are the POD modes and must come preallocated.
		S(n)     are the singular values.
		V(n,n)   are the right singular vectors.

		Lapack dgesvd:
			http://www.netlib.org/lapack/explore-html/d1/d7e/group__double_g_esing_ga84fdf22a62b12ff364621e4713ce02f2.html
			https://www.netlib.org/lapack/explore-html/d0/dee/lapacke__dgesvd_8c_af31b3cb47f7cc3b9f6541303a2968c9f.html
		Lapack dgesdd (more optimized):
			http://www.netlib.org/lapack/explore-html/d1/d7e/group__double_g_esing_gad8e0f1c83a78d3d4858eaaa88a1c5ab1.html
			http://www.netlib.org/lapack//explore-html/d3/d23/lapacke__dgesdd_8c_aaf227f107a19ae6021f591c4de5fdbd5.html
	*/
	// Run LAPACKE DGESVD for the single value decomposition
	double *superb;
	superb = (double*)malloc((int)(MIN(m,n))*sizeof(double));
	LAPACKE_dgesvd(
		LAPACK_COL_MAJOR, // int  		matrix_layout
					 'A', // char  		jobu
					 'A', // char  		jobvt
					   m, // int  		m
					   n, // int  		n
					   Y, // double*  	a
					   m, // int  		lda
					   S, // double *  	s
					   U, // double *  	u
					   m, // int  		ldu
					   V, // double *  	vt 
					   n, // int  		ldvt
				  superb  // double *  	superb
	);
	free(superb);
}