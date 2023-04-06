function generateReportSummary(reportTotals, teamName) {
    if (reportTotals.teamName > 5) {
        return `${teamName} + has surpassed goal with + ${reportTotals.teamName} reports`;
    }
}
