package compliance.access_control

violation[reason] {
    input.user_roles[_] == "guest"
    reason := "Guest role has system access"
}
