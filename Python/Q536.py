preorder='BCAD'
order='CBAD'
postoder=[]

def travel(preorder,order):

	if len(preorder):
		root=preorder[0]
		preorder=preorder[1:]

		inoL=order[:order.index(root)]
		inoR=order[order.index(root)+1:]
		proL=preorder[:len(inoL)]
		proR=preorder[len(inoL):]
		print(inoL,inoR,proL,proR)
		travel(proL,inoL)
		travel(proR,inoR)
		postoder.append(root)
		print (postoder)
	#inoR=order[order.index(root)+1:]


travel(preorder,order)