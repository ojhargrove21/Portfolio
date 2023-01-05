package cards;
public class Card
{
   private String name;
   public Card()
   {
      name = "";
   }
   public Card(String n)
   {
      name = n;
   }
	/**
	 * <pre>
	 * returns name
	 * ------------------------------------------------------
	 * String name=Card.getName();
	 * <pre>
	 * @return
	 */
   public String getName()
   {
      return name;
   }
	/**
	 * <pre>
	 * tests if expired returns false
	 * <pre>
	 * @return
	 */
   public boolean isExpired()
   {
      return false;
   }
	/**
	 * <pre>
	 * formats into String
	 * ------------------------------------------------------
	 * String output=Card.toString();
	 * <pre>
	 * @return
	 */
   public String toString()
   {
String output = "Card type: " + getClass().getSimpleName() + "\n";
      output += "Card holder: " + name + "\n";
return output;
   }
}
