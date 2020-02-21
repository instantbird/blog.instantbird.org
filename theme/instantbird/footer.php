<?php
//touch(dirname(__FILE__).'/functions.php');
/**
 * The template for displaying the footer.
 *
 * Contains the closing of the id=main div and all content after
 *
 * @package WordPress
 * @subpackage Twenty_Eleven
 * @since Twenty Eleven 1.0
 */
?>

	</div><!-- #main -->
</div></div><!-- #page -->
<footer id="colophon" role="contentinfo">
	<div id="footer">
		<?php do_action( 'twentyeleven_credits' ); ?>
		<p>&copy; 2007-2012 - <a href="http://www.instantbird.com/about.html">The Instantbird Team</a>.</p>
		<p class="small-text">All product names and trademarks are the property of their respective owners.
		<a href="<?php echo esc_url( __( 'http://wordpress.org/', 'twentyeleven' ) ); ?>" title="<?php esc_attr_e( 'Semantic Personal Publishing Platform', 'twentyeleven' ); ?>" rel="generator"><?php printf( __( 'Proudly powered by %s', 'twentyeleven' ), 'WordPress' ); ?></a>
		</p>
	</div>
</footer><!-- #colophon -->
<?php wp_footer(); ?>
</body>
</html>
