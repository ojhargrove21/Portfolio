package cards;

public class CardTester {

	public static void main(String[] args) {
		//creates card holder with 2 null objects
		CardHolder holder = new CardHolder(null, null);
		//creates IDCard and DriverLicense and adds them to holder
		IDCard idCard = new IDCard(1023, "jhon");
		DriverLicense license = new DriverLicense("james", 1012, "Maine", 2024);
		
		holder.addCard(idCard);
		holder.addCard(license);
		//prints holder
		System.out.println(holder.formatCards());

	}

}
