% Generated by roxygen2: do not edit by hand
% Please edit documentation in R/lazytensor_operations.R
\name{sum_reduction}
\alias{sum_reduction}
\title{Sum reduction.}
\usage{
sum_reduction(x, index)
}
\arguments{
\item{x}{A \code{LazyTensor} or a \code{ComplexLazyTensor}.}

\item{index}{A \code{character} corresponding to the reduction dimension that
should be either \strong{i} or \strong{j} to specify whether if the summation is
indexed by \strong{i} (rows), by \strong{j} (columns).}
}
\value{
A matrix corresponding to the sum reduction.
}
\description{
Sum reduction for LazyTensor.
}
\details{
\code{sum_reduction(x, index)} will return the sum reduction of \strong{x}
indexed by \strong{index}.
}
\examples{
\dontrun{
x <- matrix(runif(150 * 3), 150, 3) # arbitrary R matrix, 150 rows, 3 columns
x_i <- LazyTensor(x, index = 'i')   # creating LazyTensor from matrix x, 
                                    # indexed by 'i'

sum_reduction(x_i, "i")
}
}
\seealso{
\code{\link[=sum]{sum()}}
}
\author{
Chloe Serre-Combe, Amelie Vernay
}
