


Edges = [
        (list(Points[y][:dims+1] - Points[x][:dims+1])),

        #side effects
        #EdgeCorners[x].append(y=len(Edges)-1, 1),
        #EdgeCorners[y].append(x=len(Edges)-1,-1)
        for x in Points for y in Points if x<y 
        ]



