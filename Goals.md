# Payroll System - Goals
> This is a list for the things I want to achieve when building the Payroll System

## 1. Company Registration Page
### Company Name 
> The Desired Name for the Company
### Positions (Optional)
- Add Position
    - Position Name
    - Position Rate Per Day
- Add Deductions
    - Statutory Deductions
        > eg. Taxes, Insurances, & Fees...
    - Penalties
### Contact
> Important information of the Company to establish communication
- Address
- Email
- Telephone Number
### Admin 
> Create Account for Admin Access
- Username
- Password

## 2. Sign in
> Sign-in Panel allows access to the Company Payroll. Through the user type option, the user can choose whether to operate or view the payroll.
### User
- Username
- Password
- Confirm Password 
- User Type
    - Admin
    > to apply for admin access, password from an existing admin is needed
    - Employee

## 3. Login Page
> The Gate way to access the Payroll, if it exists.. 
### Credentials
- Username (Only Accepts String)
- Password (Show Toggle)

### Buttons
- Login Button
    - Catch Error
        - Empty Entry Warning
        - Wrong Credentials Warning
        - Open User Type Dashboard
- Sign-in Button
    - Close Login Page
    - Open Sign-in Page
- Register Button
    - Close Login Page
    - Open Company Registration Page
## 4. Dashboard
### Management (Admin Access)
- Positions
    - Rates
    - Allowances or other Additional pay (Applied to all)
    - Added Pay (Individual)

- Deductions
    - Statutory Deductions (Applied to all)
    - Penalties (to those that apply)
    - Etc. (If theres anything else to add)

- Employees 
    - Names
    - IDs
    - Absences & Lates
    - Overtime

- Payroll Management
    - Positions
    > add the IDs of employees to the positions. I believe this method can save time
    - Penalties
    > employees will be checked if commited lates or absences. Deduct penalties that apply
    - Added Pay (Individual)
    > employees will be checked if eligible for Overtime pay or some extra bonuses if theres any. add bonuses that apply
    - Allowances or other Additional pay (Applied to all)

- Payroll Summary Report (Table Format)
    - Employee IDs
    - Employee Names
    - Employee Positions
    - Employee Rates
    - Employee Gross
    - Employee Deductions
    - Employee + 
    - Employee Net Pay

### View-Only (Employee Access)
- Profile
    - Name
    - ID
    - Position
    - Salary Rate
- Salary Payroll Report
    - Name
    - Rate
    - Gross
    - Deduction
    - Net Pay


## 5. DataBase
- Company

- Accounts

- Employees

- Positions

- Deductions

- Payroll