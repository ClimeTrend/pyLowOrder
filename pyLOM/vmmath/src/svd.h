/*
	SVD - Singular Value Decomposition of a matrix
*/
int qr(double *Q, double *R, double *A, const int m, const int n);
int svd(double *U, double *S, double *VT, double *Y, const int m, const int n);
int tsqr_svd(double *Ui, double *S, double *VT, double *Ai, const int m, const int n, MPI_Comm comm);