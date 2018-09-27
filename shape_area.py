import geopandas
import pandas as pd

for i in range(47):
    f_num = format(i+1,'02d')
    f_point = ("A32P-16_{}.shp".format(f_num))
    f_area = ("A32-16_{}.shp".format(f_num))
    print("parse_area_{}".format(f_num))

    df_point = geopandas.read_file(f_point,encoding='shift-jis')
    df_point = df_point.rename(index=str, columns = {'A32_001':'area_code','A32_002':'area_name','A32_003':'school_name','A32_004':'school_address','A32_005':'file','geometry':'geo_point'})
    df_area = geopandas.read_file(f_area,encoding='shift-jis')
    df_area = df_area.rename(index=str, columns = {'A32_006':'area_code','A32_007':'area_name','A32_008':'school_name','A32_009':'school_address','A32_010':'file','geometry':'geo_poly'})

    print("editing_area_{}".format(f_num))
    #Pandas
    f_csv = ("parsedatafile/allchudata_{}_area.csv".format(f_num))
    f_excel = ("parsedatafile/allchudata_{}_area.xlsx".format(f_num))
    result = pd.merge(df_point, df_area, on=['school_address','school_name','area_name','area_code','file'], how='outer')
    result.to_csv(f_csv)
    with pd.ExcelWriter(f_excel) as writer:
        result.to_excel(writer)

    print("done_area_{}".format(f_num))
