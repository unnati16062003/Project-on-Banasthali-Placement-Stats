def company_year_branch_ctc(df):
    year=df['Year of placement'].unique().tolist()
    year.insert(0,'Overall')
    company=df['Name of the company'].unique().tolist()
    company.insert(0,'Overall')
    branch=['CS','IT','EC','EI','EE','BT','CE']
    branch.insert(0,'Overall')
    CTC_range=['1-5LPA','6-10LPA','11-15LPA','16-20LPA','Above 20LPA']
    CTC_range.insert(0,'Overall')
    return year,company,branch,CTC_range
def show_df(df, year, company,branch,CTC_range):
    
    if year == 'Overall' and company == 'Overall' and branch =='Overall' and CTC_range =='Overall':
        temp_df = df
    if  year == 'Overall' and company == 'Overall' and branch =='Overall' and CTC_range !='Overall':
        if CTC_range=='Above 20LPA':
            df=df[df['CTC offered(LPA)']>=20]
            temp_df = df
        else:
            CTC_range=CTC_range[:-3]
            l=CTC_range.split('-')
            a,b=int(l[0]),int(l[1])
        #df['CTC offered(LPA)'] = df['CTC offered(LPA)'].astype(int)
            temp_df = df[(df['CTC offered(LPA)']>=a)& (df['CTC offered(LPA)']<=b)]
    if  year == 'Overall' and company == 'Overall' and branch !='Overall' and CTC_range =='Overall':
        temp_df = df[df['Branch'] == branch]
    if  year == 'Overall' and company == 'Overall' and branch !='Overall' and CTC_range !='Overall':
        if CTC_range=='Above 20LPA':
            df=df[df['CTC offered(LPA)']>=20]
        else:
            CTC_range=CTC_range[:-3]
            l=CTC_range.split('-')
            a,b=int(l[0]),int(l[1])
            df = df[(df['CTC offered(LPA)']>=a)& (df['CTC offered(LPA)']<=b)]
        temp_df=df[(df['Branch'] == branch)]
    if  year == 'Overall' and company != 'Overall' and branch =='Overall' and CTC_range =='Overall':
        temp_df = df[df['Name of the company']==company]
    if  year == 'Overall' and company != 'Overall' and branch =='Overall' and CTC_range !='Overall':
        if CTC_range=='Above 20LPA':
            df=df[df['CTC offered(LPA)']>=20]
        else:
            CTC_range=CTC_range[:-3]
            l=CTC_range.split('-')
            a,b=int(l[0]),int(l[1])
            df = df[(df['CTC offered(LPA)']>=a)& (df['CTC offered(LPA)']<=b)]
        temp_df = df[(df['Name of the company']==company)]
    if  year == 'Overall' and company != 'Overall'and branch !='Overall'and CTC_range =='Overall':
        temp_df = df[(df['Name of the company']==company)&(df['Branch']==branch)]   
    if  year == 'Overall' and company != 'Overall' and branch !='Overall' and CTC_range !='Overall':
        if CTC_range=='Above 20LPA':
            df=df[df['CTC offered(LPA)']>=20]
        else:
            CTC_range=CTC_range[:-3]
            l=CTC_range.split('-')
            a,b=int(l[0]),int(l[1])
            df = df[(df['CTC offered(LPA)']>=a)& (df['CTC offered(LPA)']<=b)]
        temp_df = df[(df['Name of the company']==company)&(df['Branch']==branch)] 
    if  year != 'Overall' and company == 'Overall' and branch =='Overall' and CTC_range =='Overall':
        temp_df = df[df['Year of placement'] == year]
    if  year != 'Overall' and company == 'Overall' and branch =='Overall' and CTC_range !='Overall':
        if CTC_range=='Above 20LPA':
            df=df[df['CTC offered(LPA)']>=20]
        else:
            CTC_range=CTC_range[:-3]
            l=CTC_range.split('-')
            a,b=int(l[0]),int(l[1])
            df = df[(df['CTC offered(LPA)']>=a)& (df['CTC offered(LPA)']<=b)]
        temp_df = df[(df['Year of placement'] == year)]  
    if  (year != 'Overall') and (company == 'Overall') and (branch !='Overall') and (CTC_range =='Overall'):
        temp_df=df[(df['Year of placement'] == year)&(df['Branch']==branch)]
    if  year != 'Overall' and company == 'Overall' and branch !='Overall' and CTC_range !='Overall':
        if CTC_range=='Above 20LPA':
            df=df[df['CTC offered(LPA)']>=20]
        else:
            CTC_range=CTC_range[:-3]
            l=CTC_range.split('-')
            a,b=int(l[0]),int(l[1])
            df = df[(df['CTC offered(LPA)']>=a)& (df['CTC offered(LPA)']<=b)]
        temp_df=df[(df['Year of placement']== year) & (df['Branch']==branch)]
    if  year != 'Overall' and company != 'Overall' and branch =='Overall' and CTC_range =='Overall':
        temp_df=df[(df['Name of the company']==company)&(df['Year of placement']==year)]    
    if  year != 'Overall' and company != 'Overall' and branch =='Overall' and CTC_range !='Overall':
        if CTC_range=='Above 20LPA':
            df=df[df['CTC offered(LPA)']>=20]
        else:    
            CTC_range=CTC_range[:-3]
            l=CTC_range.split('-')
            a,b=int(l[0]),int(l[1])
            df = df[(df['CTC offered(LPA)']>=a)& (df['CTC offered(LPA)']<=b)]
        temp_df=df[(df['Name of the company']==company)&(df['Year of placement']==year)]  
    if  year != 'Overall' and company != 'Overall' and branch !='Overall' and CTC_range =='Overall':
        temp_df=df[(df['Name of the company']==company)&(df['Year of placement']==year)&(df['Branch']==branch)]
    if  year != 'Overall' and company != 'Overall' and branch !='Overall' and CTC_range !='Overall':
        if CTC_range=='Above 20LPA':
            df=df[df['CTC offered(LPA)']>=20]
        else:
            CTC_range=CTC_range[:-3]
            l=CTC_range.split('-')
            a,b=int(l[0]),int(l[1])
            
            df = df[(df['CTC offered(LPA)']>=a)& (df['CTC offered(LPA)']<=b)]
        temp_df=df[(df['Name of the company']==company)&(df['Year of placement']==year)&(df['Branch']==branch)]     
    return temp_df  

  
