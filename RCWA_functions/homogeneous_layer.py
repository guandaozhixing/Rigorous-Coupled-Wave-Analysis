import numpy as np
from scipy.linalg import block_diag
import cmath;

def homogeneous_module(Kx, Ky, e_r, m_r = 1):
    '''
    homogeneous layer is much simpler to do, so we will create an isolated module to deal with it
    :return:
    '''
    i = cmath.sqrt(-1);
    N = len(Kx);
    I = np.matrix(np.identity(N));
    P = (e_r**-1)*np.block([[Kx*Ky, e_r*m_r*I-Kx**2], [Ky**2-m_r*e_r*I, -Ky*Kx]])
    Q = (e_r/m_r)*P;
    W = np.matrix(np.identity(2*N))
    arg = (m_r*e_r*I-Kx**2-Ky**2); #arg is +kz^2
    arg = arg.astype('complex');

    Kz = np.conj(np.sqrt(arg)); #conjugate enforces the negative sign convention (we also have to conjugate er and mur if they are complex)
    eigenvalues = block_diag(i*Kz, i*Kz) #determining the modes of ex, ey... so it appears eigenvalue order MATTERS...
    V = Q*np.linalg.inv(eigenvalues); #eigenvalue order is arbitrary (hard to compare with matlab

    return W,V,Kz

def homogeneous_1D(Kx, e_r, m_r = 1):
    '''
    efficient homogeneous 1D module
    :param Kx:
    :param e_r:
    :param m_r:
    :return:
    '''
    i = cmath.sqrt(-1);

    I = np.identity(len(Kx));
    P = e_r*I - Kx**2;
    Q = I;
    arg = (m_r*e_r*I-Kx**2); #arg is +kz^2
    arg = arg.astype('complex');

    Kz = np.conj(np.sqrt(arg)); #conjugate enforces the negative sign convention (we also have to conjugate er and mur if they are complex)
    eigenvalues = i*Kz #determining the modes of ex, ey... so it appears eigenvalue order MATTERS...
    V = np.matmul(Q,eigenvalues); #eigenvalue order is arbitrary (hard to compare with matlab
    return np.matrix(I),np.matrix(V), np.matrix(Kz)


