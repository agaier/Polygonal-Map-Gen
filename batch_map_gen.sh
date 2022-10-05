
for rep in {0..6}
    do
    cmdstr="python polymap/new_map.py --n_cells=1000 --seed=$rep --fname maps/map$rep --export='all'"
    echo $cmdstr
    $cmdstr &
done