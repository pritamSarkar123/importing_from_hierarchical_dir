from same_dir import *
# in django we have to do   --> # from .same_dir import * <-- for getting files in samedir
gandu = Gandu()
print(gandu.name)
funcOne()
funcTwo()
if __name__ == "__main__":
    import sys
    # it leads to the outer dir #further appending leads to next outer dir
    sys.path.append('../')
    from supportive_dir.supporting_dir import *
    gunda = Gunda()
    print(gunda.name)
    funcThree()
    funcFour()

    # importing from next outer dir
    sys.path.append('../../')
    from outer import *
    funcOuterOne()
    funcOuterTwo()
