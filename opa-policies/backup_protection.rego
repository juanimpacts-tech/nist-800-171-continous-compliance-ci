package compliance.backup_protection

violation[reason] {
    not input.backups_encrypted
    reason := "Backups are not encrypted"
}
