
# format method is used before "f" string method

# here is f string method
hello=' this me'
a=f"{hello},Md.Shagor"
print(a)

# here is the format method
name=" Md.Shagor "
trying=" he is trying hard with his mouth"
c="His name is{}and he wanted to be a programmar but{}".format(name,trying)
# c="His name is{1}and he wanted to be a programmar but{0}".format(name,trying) set the formate

print(c)