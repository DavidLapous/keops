% Generated by roxygen2: do not edit by hand
% Please edit documentation in R/lazytensor_operations.R
\name{Re}
\alias{Re}
\title{Element-wise real part of complex.}
\usage{
Re(z)
}
\arguments{
\item{z}{A \code{ComplexLazyTensor} or any type of values accepted by R default
\code{Re()} function.}
}
\value{
An object of class "ComplexLazyTensor" if the function is called with
a \code{ComplexLazyTensor}, else see R default \code{Re()} function.
}
\description{
Symbolic unary operation for element-wise real part of complex.
}
\details{
If \code{z} is a \code{ComplexLazyTensor}, \code{Re(z)} returns a
\code{ComplexLazyTensor} that encodes, symbolically, the element-wise real part
of complex \code{z} ; else, computes R default \code{Re()} function.
}
\examples{
\dontrun{
z <- matrix(2 + 1i^ (-6:5), nrow = 4)        # complex matrix
z_i <- LazyTensor(z, "i", is_complex = TRUE) # creating ComplexLazyTensor

Re_z <- Re(z_i)                              # symbolic matrix
}
}
\author{
Chloe Serre-Combe, Amelie Vernay
}
