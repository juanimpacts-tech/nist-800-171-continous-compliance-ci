package compliance.remote_access

violation[reason] {
    input.remote_access
    reason := "Remote access is enabled without MFA"
}
