from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'RFQ Quotation for Injection Molding Tooling', 0, 1, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(5)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

pdf = PDF()

pdf.add_page()
pdf.set_left_margin(10)
pdf.set_right_margin(10)

pdf.chapter_title("Company Name: ABC Molding Solutions")
pdf.chapter_body("Address: 123 Industrial Park, Shenzhen, China\nPhone: +86 755 1234 5678\nEmail: sales@abcmolding.com\nDate: June 26, 2024")

pdf.chapter_title("Customer Information")
pdf.chapter_body("Customer Name: XYZ Manufacturing Co.\nCustomer Address: 456 Business Avenue, Los Angeles, CA, USA\nCustomer Contact: John Doe\nCustomer Email: john.doe@xyzmanufacturing.com")

pdf.chapter_title("1. Project Overview")
pdf.chapter_body("Project Name: ABC1234 Molding Project\nProject Description: This project involves the production of high-precision plastic components for the automotive industry, requiring durable and high-quality injection molds.")

pdf.chapter_title("2. Tooling Specifications")
pdf.chapter_body("Part Name: Dashboard Panel\nPart Material: ABS Plastic\nPart Dimensions: 500mm x 300mm x 50mm\nAnnual Production Volume: 50,000 units\nExpected Tool Life: 500,000 cycles")

pdf.chapter_title("3. Mold Specifications")
pdf.chapter_body("Mold Type: Multi-cavity\nMold Material: H13 Steel\nNumber of Cavities: 4\nMold Base: DME Standard\nRunner System: Hot Runner\nEjection System: Pin Ejection\nCooling System: Optimized Cooling Channels\nSurface Finish: SPI A-2 Finish")

pdf.chapter_title("4. Lead Time")
pdf.chapter_body("Design Lead Time: 2 weeks\nManufacturing Lead Time: 6 weeks\nTotal Lead Time: 8 weeks")

pdf.chapter_title("5. Pricing")
pdf.chapter_body("Design Cost: $5,000\nMold Manufacturing Cost: $50,000\nAdditional Costs:\n- Material Cost: $2,000\n- Shipping Cost: $1,000\n- Any Other Costs: $500\nTotal Cost: $58,500")

pdf.chapter_title("6. Payment Terms")
pdf.chapter_body("Payment Schedule:\n- Initial Payment: 30% ($17,550)\n- Midway Payment: 40% ($23,400)\n- Final Payment: 30% ($17,550)\nPayment Methods: Bank Transfer")

pdf.chapter_title("7. Warranty and Maintenance")
pdf.chapter_body("Warranty Period: 1 year\nMaintenance Services: Annual maintenance included for the first year.")

pdf.chapter_title("8. Terms and Conditions")
pdf.chapter_body("Delivery is FOB Shenzhen.\nQuality assurance provided as per ISO 9001 standards.\nConfidentiality agreements will be honored to protect proprietary designs.")

pdf.chapter_title("9. Contact Information")
pdf.chapter_body("Sales Representative: Jane Smith\nPhone: +86 755 8765 4321\nEmail: jane.smith@abcmolding.com\nSignature: [Jane Smith]")

pdf.output("/mnt/data/RFQ_Quotation.pdf")
