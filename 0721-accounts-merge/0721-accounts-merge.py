from collections import defaultdict

class Solution:

    def accountsMerge(self, accounts):

        n = len(accounts)

        parent = [i for i in range(n)]
        rank = [1] * n

        def find(x):

            if parent[x] != x:
                parent[x] = find(parent[x])

            return parent[x]

        def union(x, y):

            px = find(x)
            py = find(y)

            if px == py:
                return

            if rank[px] > rank[py]:
                parent[py] = px

            elif rank[py] > rank[px]:
                parent[px] = py

            else:
                parent[py] = px
                rank[px] += 1

        emailToAccount = {}

        for i, account in enumerate(accounts):

            for email in account[1:]:

                if email not in emailToAccount:
                    emailToAccount[email] = i

                else:
                    union(i, emailToAccount[email])

        mergedEmails = defaultdict(list)

        for email, accIndex in emailToAccount.items():

            parentAcc = find(accIndex)

            mergedEmails[parentAcc].append(email)

        result = []

        for parentAcc, emails in mergedEmails.items():

            result.append(
                [accounts[parentAcc][0]] + sorted(emails)
            )

        return result