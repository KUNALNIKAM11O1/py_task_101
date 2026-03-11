emails = ["chetana@speedup.com","Kunal@gmail.com","omkar@outlook.com"]

def domain(seq):
    domain_list = []
    for i in seq:
        s = i.split("@")[1]
        domain_list.append(s)
    return domain_list
print(domain(emails))      # ['speedup.com', 'gmail.com', 'outlook.com']

domains = list(map(lambda emails: emails.split("@")[1],emails))
print(domains)  # ['speedup.com', 'gmail.com', 'outlook.com']