# 💼 PAYROLL SYSTEM: LOGIN – Flowchart
```mermaid

graph TD

    %% ===== MAIN MENU =====
    A([Main Menu]) --> B[Register Company]
    A --> C[Login Page]

    %% ===== REGISTRATION =====
    B --> D{Registration Complete?}
    D -->|No| B
    D -->|Yes| C

    %% ===== LOGIN PAGE =====
    C --> E{Already Have Account?}
    E -->|Yes| F[Login: Enter Credentials]
    E -->|No| G[Register: Enter Credentials]
    C --> L[Forgot Password]

    %% ===== VALIDATION =====
    F --> H{Valid Credentials?}
    G --> H
    L --> M[Reset Password Process] --> C

    %% ===== VALIDATION RESULTS =====
    H -->|No| F
    H -->|Yes| I{User Role?}

    %% ===== DASHBOARDS =====
    I -->|Admin| J[Admin Dashboard]
    I -->|Employee| K[Employee Dashboard]

    %% ===== LOGOUT FLOW =====
    J --> N[Logout]
    K --> N
    N --> A


