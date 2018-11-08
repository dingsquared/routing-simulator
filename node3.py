from utils import TRACE, YES, NO, Rtpkt, tolayer2


class DistanceTable:
    costs = [[0 for j in range(4)] for i in range(4)]

dt = DistanceTable()

# students to write the following two routines, and maybe some others

# modify this statement for different node
edges = [7, 999, 2, 0]
node_id = 3
neighbor_id = [i for i in range(4) if edges[i]>0 and edges[i]<999]

def rtinit3():
    for i in range(4):
        if i == node_id:
            dt.costs[i] = edges
        else:
            dt.costs[i] = [999, 999, 999, 999]   
    for i in neighbor_id:
        packet = Rtpkt(node_id, i, dt.costs[node_id])
        tolayer2(packet)


def rtupdate3(rcvdpkt):
    src_id, dst_id, src_dv = rcvdpkt.sourceid, rcvdpkt.destid, rcvdpkt.mincost
    if src_id not in neighbor_id:
        print("WARNING: illegal src id in received packet, ignoring packet!\n")
        return
    if dst_id != node_id:
        print("WARNING: illegal dst id in received packet, ignoring packet!\n")
        return
    dt.costs[src_id] = src_dv
    node_dv = [min(dt.costs[node_id][j], src_dv[j]+edges[src_id]) for j in range(4)]
    if node_dv != dt.costs[node_id]:
          dt.costs[node_id] = node_dv
          for i in neighbor_id:
                packet = Rtpkt(node_id, i, node_dv)
                tolayer2(packet)


def printdt3(dtptr):
    print("             via     \n")
    print("   D3 |    0     2 \n")
    print("  ----|-----------\n")
    print("     0|  %3d   %3d\n" % (dtptr.costs[0][0], dtptr.costs[0][2]))
    print("dest 1|  %3d   %3d\n" % (dtptr.costs[1][0], dtptr.costs[1][2]))
    print("     2|  %3d   %3d\n" % (dtptr.costs[2][0], dtptr.costs[2][2]))
