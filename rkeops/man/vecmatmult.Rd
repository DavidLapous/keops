% Generated by roxygen2: do not edit by hand
% Please edit documentation in R/lazytensor_operations.R
\name{vecmatmult}
\alias{vecmatmult}
\title{Vector-matrix product.}
\usage{
vecmatmult(v, m)
}
\arguments{
\item{v}{A \code{LazyTensor} or a \code{ComplexLazyTensor} encoding a parameter vector.}

\item{m}{A \code{LazyTensor} or a \code{ComplexLazyTensor} encoding a matrix.}
}
\value{
A \code{LazyTensor} or a \code{ComplexLazyTensor}.
}
\description{
Vector-matrix product - a binary operation.
}
\details{
\code{vecmatmult(v, m)} encodes, symbolically,
the vector-matrix product of \code{v} and \code{m}.

\strong{Note}

\code{v} and \code{m} should have the same inner dimension or \code{v} should be of
dimension 1.
}
\examples{
\dontrun{
v <- c(1,2,3)                        # arbitrary R vector of length 3
m <- matrix(runif(150 * 3), 150, 3)  # arbitrary R matrix, 150 rows, 3 columns
Pm_v <- LazyTensor(v)                # parameter vector LazyTensor from v
m_i <- LazyTensor(m, index = 'i')    # LazyTensor from matrix m, indexed by 'i'

vm_mult <- vecmatmult(Pm_v, m_i)     # symbolic matrix
}
}
\author{
Chloe Serre-Combe, Amelie Vernay
}
