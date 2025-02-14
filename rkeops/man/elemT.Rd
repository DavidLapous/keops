% Generated by roxygen2: do not edit by hand
% Please edit documentation in R/lazytensor_operations.R
\name{elemT}
\alias{elemT}
\title{ElemT.}
\usage{
elemT(x, m, n)
}
\arguments{
\item{x}{A \code{LazyTensor} or a \code{ComplexLazyTensor} encoding a single
parameter value.}

\item{m}{An \code{integer} corresponding to the position \code{m} of the created
vector of zeros at which we want to insert the value \code{x}.}

\item{n}{An \code{integer} corresponding to the length of the vector of zeros.}
}
\value{
A \code{LazyTensor} or a \code{ComplexLazyTensor}.
}
\description{
Insert a given value in a symbolic vector of zeros - a unary operation.
}
\details{
\code{elemT(x, m, n)} insert scalar value \code{x} (encoded as a \code{LazyTensor}) at
position \code{m} in a vector of zeros of length \code{n}.

\strong{Note}

Input \code{x} should be a \code{LazyTensor} encoding a single parameter value.

\strong{IMPORTANT}

IN THIS CASE, INDICES START AT ZERO, therefore, \code{m} should be in \verb{[0, n)}.
}
\examples{
\dontrun{
# basic example
x <- 3.14              # arbitrary value
Pm_x <- LazyTensor(x)  # creating scalar parameter LazyTensor from x

m <- 2
n <- 3

elemT_x <- elemT(Pm_x, m, n)  # symbolic vector
}
}
\author{
Chloe Serre-Combe, Amelie Vernay
}
