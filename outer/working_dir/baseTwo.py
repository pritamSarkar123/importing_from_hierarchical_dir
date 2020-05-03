from same_dir import Gandu as G
# in django we have to do   --> # from .same_dir import Gandu as G <-- for getting files in samedir
gandu = G()
print(gandu.name)
if __name__ == "__main__":
    import sys
    # it leads to the outer dir #further appending leads to next outer dir
    sys.path.append('../')
    from supportive_dir.supporting_dir import Gunda as V
    gunda = V()
    print(gunda.name)

    # importing from next outer dir
    sys.path.append('../../')
    from outer import funcOuterOne as f
    f()
