import pygsheets


gsheet_name = "Sheet1" # change sheet name here
gsheet_url = "https://docs.google.com/spreadsheets/d/<token>/edit#gid=0" # change sheet url here


def df_to_gsheet(gsheet_url, table):
    crdname = "creds.json"
    gc = pygsheets.authorize(service_file=crdname)
    sh = gc.open_by_url(gsheet_url)
    #wks = sh[0]
    wks = sh.worksheet_by_title(gsheet_name)
    wks.append_table(values=table)


if __name__ == "__main__":
    table = ["Test", 1, 2, 3]
    df_to_gsheet(gsheet_url, table)
