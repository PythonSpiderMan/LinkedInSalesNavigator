import xlsxwriter
import json


def export_profile_to_excel(final_profile):
    filename = "output/profiles.xlsx"

    workbook = xlsxwriter.Workbook(filename)
    worksheet = workbook.add_worksheet()

    # Widen the first column to make the text clearer.
    worksheet.set_column('A:A', 20)
    worksheet.set_column('B:B', 20)
    worksheet.set_column('C:C', 20)
    worksheet.set_column('D:D', 20)
    worksheet.set_column('E:E', 20)
    worksheet.set_column('F:F', 20)
    worksheet.set_column('G:G', 20)
    worksheet.set_column('H:H', 20)
    worksheet.set_column('I:I', 20)
    worksheet.set_column('J:J', 20)
    worksheet.set_column('K:K', 20)
    worksheet.set_column('L:L', 20)
    worksheet.set_column('M:M', 20)
    worksheet.set_column('N:N', 20)

    # Formats
    title_style = workbook.add_format({'bold': True, 'align': 'left'})
    content_style = workbook.add_format({'bold': False, 'align': 'left'})

    # Write titles
    worksheet.write('A1', 'Title', title_style)
    worksheet.write('B1', 'Name', title_style)
    worksheet.write('C1', 'First Name', title_style)
    worksheet.write('D1', 'Last Name', title_style)
    worksheet.write('E1', 'Time in role', title_style)
    worksheet.write('F1', 'Twitter', title_style)
    worksheet.write('G1', 'Contact Linkedin Profile URL', title_style)
    worksheet.write('H1', 'Contact Location', title_style)
    worksheet.write('I1', 'Company', title_style)
    worksheet.write('J1', 'Company Size (Employees)', title_style)
    worksheet.write('K1', 'Industry', title_style)
    worksheet.write('L1', 'Company Profile Linkedin URL', title_style)
    worksheet.write('M1', 'Company Website', title_style)
    worksheet.write('N1', 'ID', title_style)

    for row_index in range(0, len(final_profile)):
        worksheet.write(row_index+1, 0, final_profile[row_index]['title'], content_style)
        worksheet.write(row_index+1, 0, final_profile[row_index]['name'], content_style)
        worksheet.write(row_index+1, 0, final_profile[row_index]['first_name'], content_style)
        worksheet.write(row_index+1, 0, final_profile[row_index]['last_name'], content_style)
        worksheet.write(row_index+1, 0, final_profile[row_index]['time_in_role'], content_style)
        worksheet.write(row_index+1, 0, final_profile[row_index]['twitter'], content_style)
        worksheet.write(row_index+1, 0, final_profile[row_index]['contact_linkedin_profile_url'], content_style)
        worksheet.write(row_index+1, 0, final_profile[row_index]['contact_location'], content_style)
        worksheet.write(row_index+1, 0, final_profile[row_index]['company'], content_style)
        worksheet.write(row_index+1, 0, final_profile[row_index]['company_size'], content_style)
        worksheet.write(row_index+1, 0, final_profile[row_index]['industry'], content_style)
        worksheet.write(row_index+1, 0, final_profile[row_index]['company_profile_linkedin_url'], content_style)
        worksheet.write(row_index+1, 0, final_profile[row_index]['company_website'], content_style)
        worksheet.write(row_index+1, 0, str(row_index), content_style)

    workbook.close()


def summary(final_profile):
    print("Exported all profiles to profiles.xlsx inside output folder")
    print("Total: %s profiles had exported" % (len(final_profile)))

if __name__ == '__main__':
    # Open final profile from step 6
    step_6_directory = 'temp/step_6/'
    f = open(file=step_6_directory + 'final_profiles.json', mode='rb')
    final_profile = json.loads(f.read().decode('utf-8'))
    f.close()

    export_profile_to_excel(final_profile)
    summary(final_profile)
