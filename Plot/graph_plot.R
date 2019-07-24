library(igraph)

m <- read.table(row.names=1, file=file.choose(), header=TRUE, sep = ",")
m <- as.matrix(m)
a <- graph.adjacency(m, mode = "undirected", weighted = TRUE)


