policy=$1
./build_champsim.sh bimodal no no no no $policy 1

./run_champsim.sh bimodal-no-no-no-no-$policy-1core 30 30 cadical-high-60K-134B.champsimtrace.xz
./run_champsim.sh bimodal-no-no-no-no-$policy-1core 30 30  kissat-inc-high-30K-1802B.champsimtrace.xz
./run_champsim.sh bimodal-no-no-no-no-$policy-1core 30 30 cadical-high-60K-1227B.champsimtrace.xz
