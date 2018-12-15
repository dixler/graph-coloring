#!/bin/bash

gnuplot <<EOF
set terminal "pdfcairo";
set title "10 nodes 50% probability of edges";
set output "t1_time.pdf";
set xlabel "trial";
set ylabel "seconds";
plot  'heuristic_data_10-50.dat' using 1:2 title 'heuristic execution time' with linespoints, \
      'optimal_data_10-50.dat' using 1:2 title 'optimal execution time' with linespoints;
EOF

gnuplot <<EOF
set terminal "pdfcairo";
set title "10 nodes 50% probability of edges";
set output "t1_color.pdf";
set xlabel "trial";
set ylabel "colors";
plot  'heuristic_data_10-50.dat' using 1:3 title 'heuristic colors used' with linespoints, \
      'optimal_data_10-50.dat' using 1:3 title 'optimal colors' with linespoints;
EOF
