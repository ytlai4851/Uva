a={'K':{'S':100},
	'S':{'U':80,'K':100},
	'U':{'M':120,'S':80},
	'M':{'U':120}
}
visit=set()

star='K'
end='M'

visit.add(star)
visit.add(end)

print(visit)