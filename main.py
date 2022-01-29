def main():
    age_list = [1,3,2,1,3,2,1,1,3,3,4,5,3,2,1]
    age_to_count = {}
    for a in age_list:
        if a not in age_to_count:
            age_to_count[a]=0# age occurs 0 times
        age_to_count[a]+=1
    print(age_to_count)



if __name__=='__main__':
    main()